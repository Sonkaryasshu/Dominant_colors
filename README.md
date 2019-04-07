# Dominant_colors
Identify the dominant colors from image eliminating neutral colors.

Firstly, I converted image to HSV format from BGR format to remove neutral colors.
By trying many values for the lower and upper limits, I adjusted values to best fit according to me. The finally I removed neutral colors from image.

I have used K-Means clustering to get 5 dominating colors from the image and histogram to get the percentage of domination and visualization.
Overall I have used OpenCV with KMeans for the whole project. The output of the python file contains the top 5 dominating colors with their hexcode and percentage sharing and a histogram to visualize real color(as we can't really visualize color by it's hexcode).
