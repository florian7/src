#include <iostream>
#include <array>
#include <CImg.h>

using namespace cimg_library;

class Kernel
{

public:
	typedef std::array<std::array<int, 3>, 3> kernel_3x3_t;

	template <typename T>
	static void print(CImg< T > image)
	{
		size_t w = image.width();
		size_t h = image.height();
		size_t step = w / 20;
		size_t x, y;


		for (y = 0; y < h; y += step){
			for (x = 0; x < w; x += step){
				printf("%03.0f ", image(x, y, 0));
			}
			printf("\n");
		}
		
		printf("\n");
	}

	template <typename T>
	static CImg< T > grayscale_weighted(CImg< T > image)
	{
		CImg< T > grayscale(image.width(), image.height(), 1, 1, 0);

		cimg_forXY(image, x, y){
			int R = (int) image(x, y, 0, 0);
			int G = (int) image(x, y, 0, 1);
			int B = (int) image(x, y, 0, 2);
			grayscale(x, y) = (T)(0.299 * R + 0.587 * G + 0.114 * B);
		}

		return grayscale;
	}

	template <typename T>
	static CImg< T > grayscale(CImg< T > image)
	{
		if (image.spectrum() == 3){
			CImg< T > grayscale(image.width(), image.height(), 1, 1, 0);

			cimg_forXY(image, x, y){
				int R = (int) image(x, y, 0, 0);
				int G = (int) image(x, y, 0, 1);
				int B = (int) image(x, y, 0, 2);
				grayscale(x, y) = (T)((R + G + B) / 3);
			}

			return grayscale;
		}

		else
			return image;
	}

	template <typename T>
	static CImg< T > kernel_3x3(CImg< T > image, kernel_3x3_t kernel, int normalize = 1, float norm_offset = 0)
	{
		CImg< T > new_image(image);
		CImg_3x3(N, T);

		cimg_forC(image, k){
		cimg_for3x3(image, x, y, 0, k, N, T){
			T sum = 0; 
			sum += Npp * kernel[0][0];
			sum += Npc * kernel[0][1];
			sum += Npn * kernel[0][2];
			sum += Ncp * kernel[1][0];
			sum += Ncc * kernel[1][1];
			sum += Ncn * kernel[1][2];
			sum += Nnp * kernel[2][0];
			sum += Nnc * kernel[2][1];
			sum += Nnn * kernel[2][2];
			new_image(x, y, k) = sum / normalize + norm_offset;
		}}
		

		return new_image;
	}

	template <typename T>
	static CImg< T > gaussian_blur(CImg< T > image)
	{
		kernel_3x3_t kernel;
		kernel[0] = {1,2,1};
		kernel[1] = {2,4,2};
		kernel[2] = {1,2,1};

		return kernel_3x3(image, kernel, 16);
	}

	template <typename T>
	static CImg< T > sobel_x(CImg< T > image)
	{
		kernel_3x3_t kernel;
		kernel[0] = {1,0,-1};
		kernel[1] = {2,0,-2};
		kernel[2] = {1,0,-1};

		return kernel_3x3(image, kernel);
	}

	template <typename T>
	static CImg< T > sobel_y(CImg< T > image)
	{
		kernel_3x3_t kernel;
		kernel[0] = {1,2,1};
		kernel[1] = {0,0,0};
		kernel[2] = {-1,-2,-1};

		return kernel_3x3(image, kernel);
	}

	template <typename T>
	static CImg< T > sobel_gradient(
		CImg< T > sobel_x, 
		CImg< T > sobel_y)
	{
		CImg< T > sobel_gradient(sobel_x);

		cimg_forXY(sobel_x, x, y){
			sobel_gradient(x, y) = 
				sqrt(pow(sobel_x(x, y), 2) + pow(sobel_y(x, y), 2));
		}

		return sobel_gradient;
	}
};
