# Hi-Cal Inhouse Calendar
# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

def merge_ranges(meetings):

    if meetings == []:
        return "Calendar is open!"
    else:
        #  Custom quick sort
        sorted_meetings =  sort_meetings(meetings)

        # Python's inbuilt sort
        # sorted_meetings =  sorted(meetings)

        print(sorted_meetings)
        result_array = [sorted_meetings[0]]
        i = 1
        
        while i < len(sorted_meetings):
            curr_tuple = result_array[-1]
            next_tuple = sorted_meetings[i]
            
            if curr_tuple[1] < next_tuple[0]:
                result_array.append(next_tuple)

            elif next_tuple[0] <= curr_tuple[1] < next_tuple[1]:
                result_array[-1] = (curr_tuple[0], next_tuple[1])

            
            i += 1

    return result_array



def sort_meetings(meetings): 
    low, equal, high = [], [], []

    if len(meetings) < 2:
        return meetings
        
    else:
        pivot = int(len(meetings) / 2)
        for _ in meetings:
            if _[0] < meetings[pivot][0]:
                low.append(_)
            elif _ == meetings[pivot]:
                equal.append(meetings[pivot])
            else:
                high.append(_)
                
        
    return sort_meetings(low) + equal + sort_meetings(high)

# print(merge_ranges([[9,11], (5,6), (2,3), (1,5)]))
# print(merge_ranges([]))
# print(merge_ranges([(0, 1), (9, 10), (3, 5), (4, 8), (6, 8)]))
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))


# Solution - InterviewCake
# First, we sort our input list of meetings by start time so any meetings that might need to be merged 
# are now next to each other.

# Then we walk through our sorted meetings from left to right. At each step, either:

# We can merge the current meeting with the previous one, so we do.
# We can't merge the current meeting with the previous one, so we know the previous meeting can't be 
# merged with any future meetings and we throw the current meeting into merged_meetings.


#   def merge_ranges(meetings):

#     # Sort by start time
#     sorted_meetings = sorted(meetings)

#     # Initialize merged_meetings with the earliest meeting
#     merged_meetings = [sorted_meetings[0]]

#     for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#         last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

#         # If the current meeting overlaps with the last merged meeting, use the
#         # later end time of the two
#         if (current_meeting_start <= last_merged_meeting_end):
#             merged_meetings[-1] = (last_merged_meeting_start,
#                                    max(last_merged_meeting_end,
#                                        current_meeting_end))
#         else:
#             # Add the current meeting since it doesn't overlap
#             merged_meetings.append((current_meeting_start, current_meeting_end))

#     return merged_meetings