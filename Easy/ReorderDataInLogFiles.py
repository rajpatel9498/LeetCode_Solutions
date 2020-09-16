class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digi=[]
        letters=[]
        for i in logs:
            k=i.split()
            print(k)
            if k[1].isdigit():
                digi.append(i)
            else:
                letters.append(i)
        letters = sorted(letters, key=lambda letter: (letter.split()[1:],letter.split()[0]))
        return letters+digi
# Basically sorting letter list by alphabetically first and then by identifier just in case we have a tie when sorting alphabetically.
# Recommended video to watch sorted function and lambda function: https://www.youtube.com/watch?v=F_j90A48X6M
