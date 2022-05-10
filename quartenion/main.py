import numpy as np
import quartenion as qt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Generate Quartenion Class Instance
    Q = qt.Quartenion()

    #Define Rotation Axis. Rotate a point around rot_axis
    rot_axis = np.array([0, 1, 0])

    #Coordinate point to be rotated. index 0 is always 0 number. index 1 is x axis, 2 is y , 3 is z
    xyz = np.array([0, 1, 0, 0])

    ret_array = Q.calc_rot_mat(45, rot_axis, xyz)
