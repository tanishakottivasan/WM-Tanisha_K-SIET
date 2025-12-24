# Route prioritization logic for smart waste bins

bins = [
    {"id": "BIN_01", "fill": 85, "zone": "A"},
    {"id": "BIN_02", "fill": 45, "zone": "A"},
    {"id": "BIN_03", "fill": 92, "zone": "B"},
]

priority_bins = [b for b in bins if b["fill"] >= 80]

for bin in priority_bins:
    print(f"Collect {bin['id']} from Zone {bin['zone']}")
