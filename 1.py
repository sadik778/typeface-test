def find_bounding_boxes(image):
  bounding_boxes = []

  # Loop through each pixel in the image
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      # If the current pixel is white and is not part of an existing bounding box
      if image[i, j] == 1 and not any(bbox.contains(i, j) for bbox in bounding_boxes):
        # Create a new bounding box starting at the current pixel
        bbox = BoundingBox(i, j)

        # Expand the bounding box by searching the surrounding pixels for white pixels that are not already part of the bounding box
        bbox.expand(image)

        # Add the bounding box to the list of bounding boxes
        bounding_boxes.append(bbox)

  # Return the list of bounding boxes
  return bounding_boxes
