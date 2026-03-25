import os
import torch
import matplotlib.pyplot as plt
import numpy as np

# Util function for loading meshes
from pytorch3d.io import load_objs_as_meshes, load_obj
from pytorch3d.utils import ico_sphere
# Data structures and functions for rendering
from pytorch3d.structures import Meshes, join_meshes_as_batch, join_meshes_as_scene
# from pytorch3d.vis.plotly_vis import AxisArgs, plot_batch_individually, plot_scene
# from pytorch3d.vis.texture_vis import texturesuv_image_matplotlib
from pytorch3d.renderer import (
    look_at_view_transform,
    FoVPerspectiveCameras, 
    PointLights, 
    DirectionalLights, 
    Materials, 
    RasterizationSettings, 
    MeshRenderer, 
    MeshRasterizer,  
    SoftPhongShader,
    TexturesUV,
    TexturesVertex
)

device = torch.device("cuda:0")
torch.cuda.set_device(device)
colors = np.load("colors.npy")

def sphere_mesh(color : torch.tensor, device : torch.device) -> Meshes:
    base = ico_sphere(level=3,device=device)
    verts = base.verts_packed()
    faces = base.faces_packed()
    verts_color = color[None,None,:].expand(1, verts.shape[0],3)
    textures = TexturesVertex(verts_features=verts_color)
    return Meshes(verts=[verts],faces=[faces],textures=textures)

def make_scene_mesh(meshes, positions : torch.tensor):
    return join_meshes_as_scene([m.offset_verts(pos) for m,pos in zip(meshes,positions)])

def batch_render(mesh : Meshes, poses : torch.tensor, at = torch.tensor):
    """

    """
    Rs, Ts = look_at_view_transform(eye=poses,at=at)

    cameras = FoVPerspectiveCameras(device=device, R=Rs, T=Ts, fov=120)

    raster_settings = RasterizationSettings(
        image_size=256, 
        blur_radius=0.0, 
        faces_per_pixel=2, #rasterization k-best approxes
        )
    lights = PointLights(device=device, location=[[0.0, 4.0, 0.0]]) #+Y is up - 
    renderer = MeshRenderer(
        rasterizer=MeshRasterizer(
            cameras=cameras, 
            raster_settings=raster_settings
        ),
        shader=SoftPhongShader(
            device=device, 
            cameras=cameras,
            lights=lights
        )
    )
    return renderer(mesh.extend(len(poses)))



