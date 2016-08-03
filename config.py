import astropy.units as u
import numpy as np

L1688={'size_x' : 9, 'size_y' : 7, 
    'scalebar_size' : 0.1*u.pc, 'scalebar_pos' : 'bottom right',
    'distance' : 145.*u.pc, 'beam_pos' : 'bottom left',
    'label_xpos' : 0.025, 'label_ypos' : 0.1,
    'label_align' : 'left',
    'rms_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'rms_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'mom0_min' : np.array([-0.05, -0.05, -0.05, -0.1, -0.05, -0.05, -0.05]),
    'mom0_max' : np.array([4.5, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'w11_step' : 0.3*3}
B18={'size_x' : 19, 'size_y' : 7, 
    'scalebar_size' : 0.1*u.pc, 'scalebar_pos' : 'bottom right',
    'distance' : 145.*u.pc, 'beam_pos' : 'top left',
    'label_xpos' : 0.025, 'label_ypos' : 0.9,
    'label_align' : 'left',
    'rms_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'rms_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'mom0_min' : np.array([-0.17,-0.1,-0.1,-0.3,-0.25,-0.25,-0.36]),
    'mom0_max' : np.array([3.0, 0.5, 0.5, 1.8, 1.4, 1.0, 1.5]),
    'w11_step' : 0.3}
NGC1333={'size_x' : 8, 'size_y' : 12, 
    'scalebar_size' : 0.1*u.pc, 'scalebar_pos' : 'top right',
    'distance' : 250.*u.pc, 'beam_pos' : 'bottom left',
    'label_xpos' : 0.025, 'label_ypos' : 0.075,
    'label_align' : 'left',
    'rms_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'rms_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'mom0_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'mom0_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'w11_step' : 0.3}
OrionA={'size_x' : 4.5, 'size_y' : 11, 
    'scalebar_size' : 0.1*u.pc, 'scalebar_pos' : 'bottom right',
    'distance' : 450.*u.pc, 'beam_pos' : 'top left',
    'label_xpos' : 0.025, 'label_ypos' : 0.925,
    'label_align' : 'left',
    'rms_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'rms_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'mom0_min' : np.array([0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05]),
    'mom0_max' : np.array([0.75, 0.75, 0.75, 1.0, 0.75, 0.75, 0.75]),
    'w11_step' : 0.3 }

plottingDictionary = {"L1688" : L1688, "B18" : B18, "NGC1333" : NGC1333, "OrionA" : OrionA}
