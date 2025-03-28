# Identify the "WebQTrn" section in the file
webqtrn_section = []
inside_webqtrn = False

for line in lines:
    if "WebQTrn" in line:  # Assuming this marks the start of the section
        inside_webqtrn = True
    if inside_webqtrn:
        webqtrn_section.append(line)

# Extract IDs in the WebQTrn section
webqtrn_ids = [match.group() for line in webqtrn_section for match in id_pattern.finditer(line)]

# Count occurrences of each ID
webqtrn_id_counts = Counter(webqtrn_ids)

# Find overlapping (duplicate) IDs in WebQTrn section
webqtrn_overlapping_ids = {id_: count for id_, count in webqtrn_id_counts.items() if count > 1}

# Display overlapping IDs in WebQTrn section
webqtrn_overlapping_ids
