# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class Generator(torch.nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.module_0 = py_nndct.nn.Input() #Generator::input_0
        self.module_1 = py_nndct.nn.Input() #Generator::input_1
        self.module_2 = py_nndct.nn.Linear(in_features=100, out_features=6400, bias=True) #Generator::Generator/Linear[net_noise]/1625
        self.module_3 = py_nndct.nn.Module('reshape') #Generator::Generator/1631
        self.module_4 = py_nndct.nn.Linear(in_features=4, out_features=1024, bias=True) #Generator::Generator/Linear[net_label]/1632
        self.module_5 = py_nndct.nn.Module('reshape') #Generator::Generator/1638
        self.module_6 = py_nndct.nn.Cat() #Generator::Generator/1641
        self.module_7 = py_nndct.nn.Module('permute') #Generator::Generator/1647
        self.module_8 = py_nndct.nn.ConvTranspose2d(in_channels=116, out_channels=64, kernel_size=[5, 5], stride=[2, 2], padding=[1, 1], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[0]/input.5
        self.module_9 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[1]/input.7
        self.module_10 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/Conv2d[0]/input.9
        self.module_11 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/LeakyReLU[1]/input.11
        self.module_12 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[2]/Sequential[block]/Conv2d[2]/1708
        self.module_13 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[2]/input.13
        self.module_14 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[2]/1712
        self.module_15 = py_nndct.nn.ConvTranspose2d(in_channels=64, out_channels=128, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[3]/input.15
        self.module_16 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[4]/input.17
        self.module_17 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/Conv2d[0]/input.19
        self.module_18 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/LeakyReLU[1]/input.21
        self.module_19 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[5]/Sequential[block]/Conv2d[2]/1773
        self.module_20 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[5]/input.23
        self.module_21 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[5]/1777
        self.module_22 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=256, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[6]/input.25
        self.module_23 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[7]/input.27
        self.module_24 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/Conv2d[0]/input.29
        self.module_25 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/LeakyReLU[1]/input.31
        self.module_26 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[8]/Sequential[block]/Conv2d[2]/1838
        self.module_27 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[8]/input.33
        self.module_28 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[8]/1842
        self.module_29 = py_nndct.nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[9]/input.35
        self.module_30 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[10]/input.37
        self.module_31 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/Conv2d[0]/input.39
        self.module_32 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/LeakyReLU[1]/input.41
        self.module_33 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[11]/Sequential[block]/Conv2d[2]/1903
        self.module_34 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[11]/input.43
        self.module_35 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[11]/1907
        self.module_36 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #Generator::Generator/Sequential[net]/ConvTranspose2d[12]/input.45
        self.module_37 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/LeakyReLU[13]/input.47
        self.module_38 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/Conv2d[0]/input.49
        self.module_39 = py_nndct.nn.LeakyReLU(negative_slope=0.1015625, inplace=False) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/LeakyReLU[1]/input.51
        self.module_40 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/ResBlock[14]/Sequential[block]/Conv2d[2]/1968
        self.module_41 = py_nndct.nn.Add() #Generator::Generator/Sequential[net]/ResBlock[14]/input.53
        self.module_42 = py_nndct.nn.ReLU(inplace=False) #Generator::Generator/Sequential[net]/ResBlock[14]/input.55
        self.module_43 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[11, 11], stride=[1, 1], padding=[5, 5], dilation=[1, 1], groups=1, bias=True) #Generator::Generator/Sequential[net]/Conv2d[15]/input
        self.module_44 = py_nndct.nn.Hardsigmoid(inplace=False) #Generator::Generator/Sequential[net]/Hardsigmoid[16]/1992

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_1 = self.module_1(input=args[1])
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(input=output_module_0, shape=[1,8,8,100])
        output_module_1 = self.module_4(output_module_1)
        output_module_1 = self.module_5(input=output_module_1, shape=[1,8,8,16])
        output_module_0 = self.module_6(dim=3, tensors=[output_module_0,output_module_1])
        output_module_0 = self.module_7(dims=[0,3,1,2], input=output_module_0)
        output_module_0 = self.module_8(output_module_0)
        output_module_0 = self.module_9(output_module_0)
        output_module_10 = self.module_10(output_module_0)
        output_module_10 = self.module_11(output_module_10)
        output_module_10 = self.module_12(output_module_10)
        output_module_10 = self.module_13(input=output_module_10, other=output_module_0, alpha=1)
        output_module_10 = self.module_14(output_module_10)
        output_module_10 = self.module_15(output_module_10)
        output_module_10 = self.module_16(output_module_10)
        output_module_17 = self.module_17(output_module_10)
        output_module_17 = self.module_18(output_module_17)
        output_module_17 = self.module_19(output_module_17)
        output_module_17 = self.module_20(input=output_module_17, other=output_module_10, alpha=1)
        output_module_17 = self.module_21(output_module_17)
        output_module_17 = self.module_22(output_module_17)
        output_module_17 = self.module_23(output_module_17)
        output_module_24 = self.module_24(output_module_17)
        output_module_24 = self.module_25(output_module_24)
        output_module_24 = self.module_26(output_module_24)
        output_module_24 = self.module_27(input=output_module_24, other=output_module_17, alpha=1)
        output_module_24 = self.module_28(output_module_24)
        output_module_24 = self.module_29(output_module_24)
        output_module_24 = self.module_30(output_module_24)
        output_module_31 = self.module_31(output_module_24)
        output_module_31 = self.module_32(output_module_31)
        output_module_31 = self.module_33(output_module_31)
        output_module_31 = self.module_34(input=output_module_31, other=output_module_24, alpha=1)
        output_module_31 = self.module_35(output_module_31)
        output_module_31 = self.module_36(output_module_31)
        output_module_31 = self.module_37(output_module_31)
        output_module_38 = self.module_38(output_module_31)
        output_module_38 = self.module_39(output_module_38)
        output_module_38 = self.module_40(output_module_38)
        output_module_38 = self.module_41(input=output_module_38, other=output_module_31, alpha=1)
        output_module_38 = self.module_42(output_module_38)
        output_module_38 = self.module_43(output_module_38)
        output_module_38 = self.module_44(output_module_38)
        return output_module_38
