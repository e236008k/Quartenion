import numpy as np
import math

class Quartenion:

    def __init__(self):

        self.q = np.zeros((4, 1), dtype=float)
        self.q_inv = np.zeros((4, 1), dtype=float)

    def _set_quartenion_mat(self, theta_deg, rot_axis):

        self.q[0] = math.cos(math.radians(theta_deg/2))
        self.q[1] = math.sin(math.radians(theta_deg/2))*rot_axis[0]
        self.q[2] = math.sin(math.radians(theta_deg/2))*rot_axis[1]
        self.q[3] = math.sin(math.radians(theta_deg/2))*rot_axis[2]

        self.q_inv[0] = math.cos(math.radians(theta_deg/2))
        self.q_inv[1] = -math.sin(math.radians(theta_deg/2)) * rot_axis[0]
        self.q_inv[2] = -math.sin(math.radians(theta_deg/2)) * rot_axis[1]
        self.q_inv[3] = -math.sin(math.radians(theta_deg/2)) * rot_axis[2]

    def _get_quartenion_mult(self, mat_1, mat_2):

        ret_list = np.zeros((4,1), dtype=float)

        # definition of axis number
        w = 0
        x = 1
        y = 2
        z = 3

        # w axix(real part)
        ret_list[w] = mat_1[w] * mat_2[w] - ( mat_1[x]*mat_2[x] + mat_1[y]*mat_2[y] + mat_1[z]*mat_2[z] )

        # x axis(imaginary part)
        ret_list[x] = mat_1[w] * mat_2[x] + mat_1[x] * mat_2[w] + ( mat_1[y] * mat_2[z] - mat_1[z] * mat_2[y] )

        # y axis(imaginary part)
        ret_list[y] = mat_1[w] * mat_2[y] + mat_1[y] * mat_2[w] + (mat_1[z] * mat_2[x] - mat_1[x] * mat_2[z])

        # z axis(imaginary part)
        ret_list[z] = mat_1[w] * mat_2[z] + mat_1[z] * mat_2[w] + (mat_1[x] * mat_2[y] - mat_1[y] * mat_2[1])

        return ret_list

    def calc_rot_mat(self, theta_deg, rot_axis, xyz):

        #Quaternionの定義
        self._set_quartenion_mat(theta_deg, rot_axis)

        ans_temp = self._get_quartenion_mult( self.q, xyz )

        ans = self._get_quartenion_mult( ans_temp, self.q_inv )

        return ans