import pandas as pd
file_name = "1_binary_landscapes.txt"
file_path = "files/" + file_name
output_path = "output/" + file_name
global_satisfaction_score = 0
prev_frame_tags = []
temp_portrait_tags = []
portrait_counter = 0
local_score = 0
paintings = []
landscape_paintings = []
portrait_paintings = []

chunk_size = 10  # Number of lines to read per chunk

# Initialize an empty DataFrame
df = pd.DataFrame(columns=["Type", "Number of Tags", "Tags"])

# Read the large file in chunks
rows = []
with open(file_path, 'r') as file:
    next(file)  # Skip the first row
    for line in file:
        # Split the line by space
        data = line.strip().split(' ')
        # Extract the relevant information
        row = {
            "Type": data[0],
            "Number of Tags": data[1],
            "Tags": data[2:]
        }

        # Append the row to the DataFrame
        rows.append(row)
df = pd.DataFrame(rows)
print(df)
total_L = df[df['Type'] == 'L'].shape[0]
total_P = df[df['Type'] == 'P'].shape[0]
total_frames = total_L + total_P/2

# Write the output to a file
with open(output_path, 'w') as file:
    file.write(f"{int(total_frames)}\n")
    prev_type = ''
    for index, row in df.iterrows():
        if row['Type'] == 'L':
            if prev_type == 'P':
                file.write('\n')
            file.write(f"{index}\n")
            prev_type = 'L'
        else:
            if portrait_counter > 1:
                file.write('\n')
                portrait_counter = 0
            tags_str = str(index)
            file.write(f"{tags_str} ")
            prev_type = 'P'
            portrait_counter += 1