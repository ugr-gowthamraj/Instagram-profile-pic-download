#Make sure the below library is installed before running the code.
#pip install instaloader  
#Run the python file in your cmd
import instaloader
instaloader.Instaloader().download_profile(input("Enter the User Name: "),profile_pic_only=True)
