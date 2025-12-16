# ombre

### Shadows on the wall
This project is focused on an <strong>inverse graphics</strong> problem. In general, inverse graphics is interested in given some images of an object (such as from sensors), you want to reconstruct the object from the images and obtain some other useful information along the way. In terms of Plato's cave, this is learning about reality through shadows on the wall; and although the allegory correctly notes that one's view of reality is limited by such a simple picture, by combining multiple angles and perspectives, one is able to get a more complete idea of reality.

### The problem
Suppose that there are a series of opaque colored spheres in space, and call this the scene. You are given a few different vantage points from which to record a 2D image, and your task is to determine where they most likely are in space, but more importantly, construct some scene which would give you roughly the same images you recorded.

### Objectives
The main objective is to obtain a model which is faithful to the input images and perspectives (largely pixel-based).
Some secondary ones include trying to reduce the number of spheres used and avoiding excessive overlap between spheres.

As a fun sidenote, this could be used to kind of generate "anamorphic art" in which depending on the angle or perspective you look at it, it can be complete nonsense or form one of several different images.
