file_path = "files/110_oily_portraits.txt"
global_satisfaction_score = 0
prev_frame_tags = []
temp_portrait_tags = []
portrait_counter = 0
local_score = 0
with open(file_path, "r") as file:
    next(file)
    lines = file.readlines()
    for line in lines:
        type,  number_of_tags, *tags = line.split()
        if type.lower() == "l":
            intersection = 0
            intersection = len(set(tags) & set(prev_frame_tags))
            local_score = min(intersection, len(set(tags)) - intersection,
                              len(set(prev_frame_tags)) - intersection)
            prev_frame_tags = tags
        else:
            if portrait_counter > 0:
                set1 = set(temp_portrait_tags)
                set2 = set(tags)
                unique_list_tags = list(set1.union(set2))
                intersection = 0
                intersection = len(set(unique_list_tags) & set(prev_frame_tags))
                local_score = min(intersection, len(set(unique_list_tags)) - intersection,
                                  len(set(prev_frame_tags)) - intersection)
                portrait_counter = 0
                prev_frame_tags = unique_list_tags
            else:
                temp_portrait_tags = tags
                portrait_counter += 1

        global_satisfaction_score += local_score

print(global_satisfaction_score)