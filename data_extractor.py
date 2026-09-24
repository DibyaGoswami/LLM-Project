import random
from datasets import load_dataset
from tqdm import tqdm

DATASET_NAME = "Skylion007/openwebtext"
OUTPUT_TRAIN = "output_train.txt"
OUTPUT_VAL = "output_val.txt"
VOCAB_FILE = "vocab.txt"

TRAIN_FRACTION = 0.9
TARGET_TOTAL_BYTES = 2 * 1024**3
TARGET_TRAIN_BYTES = int(TARGET_TOTAL_BYTES * TRAIN_FRACTION)
TARGET_VAL_BYTES = TARGET_TOTAL_BYTES - TARGET_TRAIN_BYTES

random.seed(42)


def main():
    dataset = load_dataset(DATASET_NAME, split="train", streaming=True)
    dataset = dataset.shuffle(seed=42, buffer_size=10_000)

    vocab = set()
    train_bytes = 0
    val_bytes = 0

    train_file = open(OUTPUT_TRAIN, "w", encoding="utf-8")
    val_file = open(OUTPUT_VAL, "w", encoding="utf-8")

    pbar = tqdm(total=TARGET_TRAIN_BYTES + TARGET_VAL_BYTES, unit="B", unit_scale=True, desc="Extracting OpenWebText")

    try:
        for example in dataset:
            if train_bytes >= TARGET_TRAIN_BYTES and val_bytes >= TARGET_VAL_BYTES:
                break

            text = example["text"]
            vocab.update(text)
            text_bytes = len(text.encode("utf-8"))

            if random.random() < TRAIN_FRACTION and train_bytes < TARGET_TRAIN_BYTES:
                train_file.write(text)
                train_bytes += text_bytes
                pbar.update(text_bytes)
            elif val_bytes < TARGET_VAL_BYTES:
                val_file.write(text)
                val_bytes += text_bytes
                pbar.update(text_bytes)
    finally:
        train_file.close()
        val_file.close()
        pbar.close()

    with open(VOCAB_FILE, "w", encoding="utf-8") as vfile:
        for char in sorted(vocab):
            vfile.write(char + "\n")

    print(f"done: train={train_bytes/1e9:.2f}GB, val={val_bytes/1e9:.2f}GB, vocab_size={len(vocab)}")


if __name__ == "__main__":
    main()
