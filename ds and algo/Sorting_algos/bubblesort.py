'''
Bubble Sort Exercises
Now that you know how about bubble sort works, you'll implement bubble sort for
 two exercises.

Exercise 1
Sam records when they wake up every morning. Assuming Sam always wakes up in 
the same hour, use bubble sort to sort by earliest to latest.'''


wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(list):

    for _ in range(len(list)-2):
        for i_pos in range(len(list)-2):
            left = list[i_pos]
            right = list[i_pos+1]

            if left > right:
                list[i_pos] = right
                list[i_pos+1] = left
            
            else:
                pass

    return list

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")


'''
Exercise 2
Sam doesn't always go to sleep in the same hour. Given the following times Sam 
has gone to sleep, sort the times from latest to earliest.'''


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def is_time_bigger(time, time_to_compare):

    t_hours, t_min = time
    ttc_hours, ttc_min = time_to_compare

    if t_hours > ttc_hours:
        return True
    elif t_hours < ttc_hours:
        return False
    else:

        if t_min >= ttc_min:
            return True
        else:
            return False


def bubble_sort_2(list):

    for _ in range(len(list)):
        for i_pos in range(len(list)-1):
            time_left = list[i_pos]
            time_right = list[i_pos+1]

            if is_time_bigger(time=time_left, time_to_compare=time_right):
                pass
            else:
                list[i_pos] = time_right
                list[i_pos + 1] = time_left

    return list

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")