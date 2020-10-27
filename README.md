# MLB-Pitch-Data

Each type of pitch has a different movement profile in two dimensions. Curveballs, for instance, tend to break on a vertical plane as they approach the plate, while 4-seam fastballs fight the pull of gravity with the help of backspin, appearing to travel on a flat plane. Sliders and changeups, on the other hand, tend to move on a horizontal plane, in addition to having significant vertical movement themselves. Additionally, each pitch type has an associated velocity range - the aptly named fastball will generally travel at a higher velocity than an off-speed pitch like a slider. We can use these three dimensions - average velocity, average horizontal movement, and average vertical movement - to build a pitch classification model using Scikit's SVM algorithm.

Note: the SVM omits Cutters and Splitters, two relatively obscure pitches that bear significant resemblence to other, more prevalent pitch types. During model construction, these pitches were being classified with a 0% success rate. The SVM also disregards a fourth dimension, average spin rate, that led to depressed model performance. 

Data contains MLB pitching data 2016-2020. Source: baseballsavant.mlb.com
