# Certified Gluten-free Product Identifier
Use OpenCV to scan the images associated with a product to determine if a certified gluten-free logo appears. Although this program can be used to query an image for any pattern, it is well-calibrated for identifying the updated certified gluten-free logo.
![gf](https://github.com/jonathanmann/certified-gluten-free-product-identifier/blob/main/gf-query.png?raw=true)

## Quickstart
After installing OpenCV (cv2) and numpy, simply import the library and start using the function to scan images for the query image. For best results, apply the calibration as described in the following section.
```
print(query_is_in_image('gf-query.png', 'examples/gf-example2.jpg', debug=True))
```

## Calibration
Place the images you'd like to scan for the query image into a folder and supply that folder as an argument. You'll probably also want to create a folder of images that do not contain your query image to verify that you won't see too many false positives. You can use gf-scan.py to get find the appropriate threshold. The results will look like this:
```
Threshold: 0.05
False negative: 1.0, True positive: 0.0
True negative: 1.0, False positive: 0.0
Threshold: 0.1
False negative: 1.0, True positive: 0.0
True negative: 1.0, False positive: 0.0
Threshold: 0.15000000000000002
False negative: 0.9090909090909091, True positive: 0.09090909090909091
True negative: 1.0, False positive: 0.0
Threshold: 0.2
False negative: 0.45454545454545453, True positive: 0.5454545454545454
True negative: 1.0, False positive: 0.0
Threshold: 0.25
False negative: 0.18181818181818182, True positive: 0.8181818181818182
True negative: 0.9875, False positive: 0.0125
Threshold: 0.3
False negative: 0.09090909090909091, True positive: 0.9090909090909091
True negative: 0.975, False positive: 0.025
Threshold: 0.35000000000000003
False negative: 0.09090909090909091, True positive: 0.9090909090909091
True negative: 0.9, False positive: 0.1
Threshold: 0.4
False negative: 0.0, True positive: 1.0
True negative: 0.65, False positive: 0.35
Threshold: 0.45
False negative: 0.0, True positive: 1.0
True negative: 0.5, False positive: 0.5
```

Set your threshold according to your preferred balance between false positives and false negatives.

## Debugging
To see what is going on "under the hood", you can set the "debug" option within the query_is_in_image function as shown below:
```
query_is_in_image('gf-query.png', image, threshold=.25,debug=True)
```
This option will display a visualization of where (if at all the query image was detected).
![example1](https://github.com/jonathanmann/certified-gluten-free-product-identifier/blob/main/examples/gf-detect1.png?raw=true)
![example2](https://github.com/jonathanmann/certified-gluten-free-product-identifier/blob/main/examples/gf-detect2.png?raw=true)

# Motivation
While I've wanted to make this certified gluten free logo detector for a while, the main reason I wanted to create this program was to test out Copilot. It did not disappoint.
