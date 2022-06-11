from ast import arg
import sys
import os

try:
    from object_detector.object_detector import ExtractImages
except:
    sys.exit("""
object_detector not installed. Please run:

    pip install object_detector 
    """)
    
arg1 = sys.argv[1]

if arg1=="list":
    os.system("svn ls https://github.com/Uncoded-AI/Object-Detection-Models/trunk/")

elif arg1=="install":
    os.system(f"svn export https://github.com/Uncoded-AI/Object-Detection-Models/trunk/{sys.argv[2]} /lib/objectdetector/weights")

# print(sys.argv[1])
# # a = ExtractImages()