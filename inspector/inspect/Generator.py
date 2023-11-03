# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class Generator(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(Generator, self).__init__()
        self.module_0 = py_nndct.nn.Module('nndct_const') #Generator::2687(Generator::nndct_const_0)
        self.module_1 = py_nndct.nn.Module('nndct_const') #Generator::2689(Generator::nndct_const_1)
        self.module_2 = py_nndct.nn.Input() #Generator::input_0(Generator::nndct_input_2)
        self.module_3 = py_nndct.nn.Input() #Generator::input_1(Generator::nndct_input_3)
        self.module_4 = py_nndct.nn.Linear(in_features=100, out_features=6400, bias=True) #Generator::Generator/Linear[net_noise]/ret.5(Generator::nndct_dense_4)
        self.module_5 = py_nndct.nn.Module('nndct_reshape') #Generator::Generator/ret.7(Generator::nndct_reshape_5)
        self.module_6 = py_nndct.nn.Linear(in_features=4, out_features=1024, bias=True) #Generator::Generator/Linear[net_label]/ret.9(Generator::nndct_dense_6)
        self.module_7 = py_nndct.nn.Module('nndct_reshape') #Generator::Generator/ret.11(Generator::nndct_reshape_7)
        self.module_8 = py_nndct.nn.Cat() #Generator::Generator/ret.13(Generator::nndct_concat_8)
        self.module_9 = py_nndct.nn.Module('nndct_permute') #Generator::Generator/ret.15(Generator::nndct_permute_9)
        self.module_10 = py_nndct.nn.ConvTranspose2d(in_channels=116, out_channels=64, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[1, 1], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[0]/ret.17(Generator::nndct_conv_transpose_2d_10)
        self.module_11 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[1]/ret.19(Generator::nndct_leaky_relu_11)
        self.module_12 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/Conv2d[0]/ret.21(Generator::nndct_conv2d_12)
        self.module_13 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/LeakyReLU[1]/ret.23(Generator::nndct_leaky_relu_13)
        self.module_14 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/Conv2d[2]/ret.25(Generator::nndct_conv2d_14)
        self.module_15 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[2]/ret.27(Generator::nndct_elemwise_add_15)
        self.module_16 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[2]/ret.29(Generator::nndct_relu_16)
        self.module_17 = py_nndct.nn.ConvTranspose2d(in_channels=64, out_channels=128, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[1, 1], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[3]/ret.31(Generator::nndct_conv_transpose_2d_17)
        self.module_18 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[4]/ret.33(Generator::nndct_leaky_relu_18)
        self.module_19 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/Conv2d[0]/ret.35(Generator::nndct_conv2d_19)
        self.module_20 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/LeakyReLU[1]/ret.37(Generator::nndct_leaky_relu_20)
        self.module_21 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/Conv2d[2]/ret.39(Generator::nndct_conv2d_21)
        self.module_22 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[5]/ret.41(Generator::nndct_elemwise_add_22)
        self.module_23 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[5]/ret.43(Generator::nndct_relu_23)
        self.module_24 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=256, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[1, 1], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[6]/ret.45(Generator::nndct_conv_transpose_2d_24)
        self.module_25 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[7]/ret.47(Generator::nndct_leaky_relu_25)
        self.module_26 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/Conv2d[0]/ret.49(Generator::nndct_conv2d_26)
        self.module_27 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/LeakyReLU[1]/ret.51(Generator::nndct_leaky_relu_27)
        self.module_28 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/Conv2d[2]/ret.53(Generator::nndct_conv2d_28)
        self.module_29 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[8]/ret.55(Generator::nndct_elemwise_add_29)
        self.module_30 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[8]/ret.57(Generator::nndct_relu_30)
        self.module_31 = py_nndct.nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[1, 1], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[9]/ret.59(Generator::nndct_conv_transpose_2d_31)
        self.module_32 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[10]/ret.61(Generator::nndct_leaky_relu_32)
        self.module_33 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/Conv2d[0]/ret.63(Generator::nndct_conv2d_33)
        self.module_34 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/LeakyReLU[1]/ret.65(Generator::nndct_leaky_relu_34)
        self.module_35 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/Conv2d[2]/ret.67(Generator::nndct_conv2d_35)
        self.module_36 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[11]/ret.69(Generator::nndct_elemwise_add_36)
        self.module_37 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[11]/ret.71(Generator::nndct_relu_37)
        self.module_38 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[1, 1], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[12]/ret.73(Generator::nndct_conv_transpose_2d_38)
        self.module_39 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[13]/ret.75(Generator::nndct_leaky_relu_39)
        self.module_40 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/Conv2d[0]/ret.77(Generator::nndct_conv2d_40)
        self.module_41 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/LeakyReLU[1]/ret.79(Generator::nndct_leaky_relu_41)
        self.module_42 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/Conv2d[2]/ret.81(Generator::nndct_conv2d_42)
        self.module_43 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[14]/ret.83(Generator::nndct_elemwise_add_43)
        self.module_44 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[14]/ret.85(Generator::nndct_relu_44)
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[11, 11], stride=[1, 1], padding=[5, 5], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/Conv2d[15]/ret.87(Generator::nndct_conv2d_45)
        self.module_46 = py_nndct.nn.Hardsigmoid(inplace=False) #Generator::Generator/Sequential[net]/Hardsigmoid[16]/ret.89(Generator::nndct_hsigmoid_46)
        self.module_47 = py_nndct.nn.Module('nndct_elemwise_mul') #Generator::Generator/ret.91(Generator::nndct_elemwise_mul_47)
        self.module_48 = py_nndct.nn.Sub() #Generator::Generator/ret(Generator::nndct_elementwise_sub_48)

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(data=2.0, dtype=torch.float, device='cuda')
        output_module_1 = self.module_1(data=1.0, dtype=torch.float, device='cuda')
        output_module_2 = self.module_2(input=args[0])
        output_module_3 = self.module_3(input=args[1])
        output_module_2 = self.module_4(output_module_2)
        output_module_2 = self.module_5(input=output_module_2, shape=[4,8,8,100])
        output_module_3 = self.module_6(output_module_3)
        output_module_3 = self.module_7(input=output_module_3, shape=[4,8,8,16])
        output_module_2 = self.module_8(dim=3, tensors=[output_module_2,output_module_3])
        output_module_2 = self.module_9(dims=[0,3,1,2], input=output_module_2)
        output_module_2 = self.module_10(output_module_2)
        output_module_2 = self.module_11(output_module_2)
        output_module_12 = self.module_12(output_module_2)
        output_module_12 = self.module_13(output_module_12)
        output_module_12 = self.module_14(output_module_12)
        output_module_12 = self.module_15(input=output_module_12, other=output_module_2, alpha=1)
        output_module_12 = self.module_16(output_module_12)
        output_module_12 = self.module_17(output_module_12)
        output_module_12 = self.module_18(output_module_12)
        output_module_19 = self.module_19(output_module_12)
        output_module_19 = self.module_20(output_module_19)
        output_module_19 = self.module_21(output_module_19)
        output_module_19 = self.module_22(input=output_module_19, other=output_module_12, alpha=1)
        output_module_19 = self.module_23(output_module_19)
        output_module_19 = self.module_24(output_module_19)
        output_module_19 = self.module_25(output_module_19)
        output_module_26 = self.module_26(output_module_19)
        output_module_26 = self.module_27(output_module_26)
        output_module_26 = self.module_28(output_module_26)
        output_module_26 = self.module_29(input=output_module_26, other=output_module_19, alpha=1)
        output_module_26 = self.module_30(output_module_26)
        output_module_26 = self.module_31(output_module_26)
        output_module_26 = self.module_32(output_module_26)
        output_module_33 = self.module_33(output_module_26)
        output_module_33 = self.module_34(output_module_33)
        output_module_33 = self.module_35(output_module_33)
        output_module_33 = self.module_36(input=output_module_33, other=output_module_26, alpha=1)
        output_module_33 = self.module_37(output_module_33)
        output_module_33 = self.module_38(output_module_33)
        output_module_33 = self.module_39(output_module_33)
        output_module_40 = self.module_40(output_module_33)
        output_module_40 = self.module_41(output_module_40)
        output_module_40 = self.module_42(output_module_40)
        output_module_40 = self.module_43(input=output_module_40, other=output_module_33, alpha=1)
        output_module_40 = self.module_44(output_module_40)
        output_module_40 = self.module_45(output_module_40)
        output_module_40 = self.module_46(output_module_40)
        output_module_40 = self.module_47(input=output_module_40, other=output_module_0)
        output_module_40 = self.module_48(input=output_module_40, other=output_module_1, alpha=1)
        return output_module_40
