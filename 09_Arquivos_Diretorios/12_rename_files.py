# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    i = 1
    cont = 121
    # C:/Users\x_kat\Pictures\CURSO_PRANDIANO_2019\TEste
    # C:\Users\x_kat\Pictures\CURSO_PRANDIANO_2019\P2_2020\Aula02_01_05
    nomeArq = 'C:/Users/x_kat/Pictures/CURSO_PRANDIANO_2019/P3_2020/Aula02_02_23/'
    print(nomeArq)
    for filename in os.listdir(nomeArq):
        src = nomeArq + filename
        dst = nomeArq + str(cont).zfill(3) + ".jpg"

        # rename() function will
        # rename all the files
        os.rename(src, dst)

        # print ("src: " + src)

        # print ("dst: " + dst)

        i += 1
        cont += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
