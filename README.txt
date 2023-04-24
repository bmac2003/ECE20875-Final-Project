Purdue ECE20875 Python Data Science Final Project

Unfortunately my code for this project is lost because it was stored in an folder with no backup on my previous computer that I was unable to recover.  The report describes the techniques I used to conduct the analysis so hopefully my project can be understood even without the programs written for it.
This report can be found in report.pdf

This is the assignment description for the path that I chose:

## Path 2: Student performance related to video-watching behavior

`behavior-performance.txt` contains data for an online course on how students watched videos (e.g., how much time they spent watching, how often they paused the video, etc.) and how they performed on in-video quizzes. `readme.pdf` details the information contained in the data fields. There might be some extra data fields present than the ones mentioned here. Feel free to ignore/include them in your analysis. In this path, the analysis questions we would like you to answer are as follows:
_You will run prediction algorithm(s) for __ALL__ students for __ONE__ video, and repeat this process for all videos._
1. How well can the students be naturally grouped or clustered by their video-watching behavior (`fracSpent`, `fracComp`, `fracPaused`, `numPauses`, `avgPBR`, `numRWs`, and `numFFs`)? You should use all students that complete at least five of the videos in your analysis.
`Hints: KMeans or distribution parameters(mean and standard deviation) of Gaussians`
2. Can student's video-watching behavior be used to predict a student's performance (i.e., average score `s` across all quizzes)?
3. Taking this a step further, how well can you predict a student's performance on a *particular* in-video quiz question (i.e., whether they will be correct or incorrect) based on their video-watching behaviors while watching the corresponding video? You should use all student-video pairs in your analysis.
