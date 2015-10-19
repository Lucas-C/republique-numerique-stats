import csvkit, sys
from collections import defaultdict

writer = csvkit.writer(sys.stdout)
with open(sys.argv[1]) as csv_file:
    for i, row in enumerate(csvkit.reader(csv_file)):
        if i == 0:
            col_count = len(row) - 1
            freqs = [defaultdict(int) for col in range(col_count)]
            continue
        for col in range(col_count):
            freqs[col][int(row[col + 1])] += 1
    values = sum((freqs[col].keys() for col in range(col_count)), [])
    for val in sorted(set(values)):
        val_freqs = [freqs[col][val] for col in range(col_count)]
        row = [val] + val_freqs
        writer.writerow(row)
