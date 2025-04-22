## Total Sky Imager - Team Harrow (Team Name: "Better Name Pending") <br/>
A team of 4 students competing in the HKU Computer Science Department x Hong Kong Observatory Total Sky Imager Competition to design a self contained device that captures, analyizes, and outputs the cloud cover in oktas. 

Team Members: 
- Clement Tong (Harrow HK 24', Cambridge Engineering 28')
- Edward Wei (Harrow HK 23', Cambridge Engineering 27')
- Callum Sanders (Harrow HK 24')
- Cyrus Chow (Harrow HK 24')
  
Our team decided to adopt the approach of using a sub 1000HKD ($100USD) Xiaomi mobile phone attached to one of the widest fisheye external lenses avilable for smartphones to capture the sky. It is enclosed in a 3D printed waterproof casing with an acrylic dome, and it was to be powered via solar power. 
We managed to develop a computer vision algorithm that detects the sky, clouds, lens flares, the sun, and more edge cases by colour fingerprints and implemented an android app to run the algorithm before the Covid-19 pandemic was hit and the competition was postponed.

Competition Link: https://i.cs.hku.hk/~sky/SkyImager-English.php

Sample Segmentation Results Using RGB signatures <br/>
(There are limitations to this approach (implemented in 2019). In 2025, new, computationally efficient machine learning image segmentation algorithms are avilable - eg: YOLO v8-seg)
<p align="center">
  <img src="https://github.com/tongclement/Total-Sky-Imager/assets/47275378/566f662b-a965-436a-ab45-ae9fc5cacc36" alt="LQz_astrotest1" style="width: 300px; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/b5e148b5-7ef7-4717-95cc-e2e8abff6089" alt="astrotest-seg" style="width: 300px;">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/b10ec993-008a-4a9d-aa0d-864efb6bb4b8" alt="TaiMoShanMixedLand" style="width: 300px; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/7cd30203-2458-4dba-a516-fcf3fe1d1b74" alt="TaiMoShan-MixedLand-Crop-Seg" style="width: 300px;">
</p>
Legend: Purple annotations indicates a "dark" cloud, and White annotations indicate a "light" coloured cloud <br/>

<br/>
One of the initial tests conducted to identify the RGB signatures of different sky features, such as clouds and clear sky:

<p align="center">
  <img src="https://github.com/user-attachments/assets/8d476f8a-5f4d-4a69-88e8-685b036942ff" alt="bluewhitecropped" style="width: 200px; margin-right: 10px;">
  <img src="https://github.com/tongclement/Total-Sky-Imager/assets/47275378/003819fc-49e1-40b3-b942-1abc5f49e956" alt="Blueskyvswhiteclouds" style="width: 400px;">
</p>

Figure to the left: Cropped image of the sky, containing a region with no clouds, and a region with cloud cover. Figure to the right: Histogram of the luminance of the blue channel of the image





 

