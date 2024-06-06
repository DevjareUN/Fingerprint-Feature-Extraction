import cv2
import fingerprint_feature_extractor


img = cv2.imread('enhanced/3.jpg', 0)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
FeaturesTerminations, FeaturesBifurcations, OutputImage = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=False, saveResult = True)
cv2.imwrite("result.png", OutputImage)