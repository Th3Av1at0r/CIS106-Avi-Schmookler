# this program takes grades from a .txt file and takes the average,
# the highest, and the lowest and presents them


def get_scores_file():
    try:
        import os
        scores_file = open("scores.txt", "r")
        filesize = os.path.getsize("scores.txt")
        if filesize == 0:
            print("The file is empty, exiting code")
            exit()
        else:
            next(scores_file)
        
    except IOError:
        print("File not accessible")
    
    return scores_file
    

def get_scores_lst(scores_file):
    scores_lst = []
    for line in scores_file:
        if (",") in line:
            lne_splt = line.split(",")
            lne_1 = lne_splt[1]
            lne_strp = lne_1.strip("\n")
            lne_intr = int(lne_strp)
            scores_lst.append(lne_intr)
        else:
            print("The file is formatted incorrectly, exiting code.")
            exit()
    
    return scores_lst
    

def get_average_score(scores_lst):    
    average_score = (sum(scores_lst) / len(scores_lst))
    average_score = format(average_score, '.2f')
    
    return average_score
    

def get_highest_score(scores_lst):    
    highest_score = max(scores_lst)
    
    return highest_score
    
    
def get_lowest_score(scores_lst):
    lowest_score = min(scores_lst)
    
    return lowest_score
    
    
def display_result(average_score, highest_score, lowest_score, scores_lst):
    print("The scores are " + str(scores_lst) + "\nThe class average is " + 
        str(average_score) + ", the highest grade in the class was " + 
        str(highest_score) + ", and the lowest grade was " + str(lowest_score))
    

def main():
    scores_file = get_scores_file()
    scores_lst = get_scores_lst(scores_file)
    average_score = get_average_score(scores_lst)
    highest_score = get_highest_score(scores_lst)
    lowest_score = get_lowest_score(scores_lst)
    display_result(average_score, highest_score, lowest_score, scores_lst)
    

main()
