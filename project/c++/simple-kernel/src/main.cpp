#include <iostream>
#include <CImg.h>

#include "kernel.h"

using namespace cimg_library;

typedef float pix_t;

int main (int argc, char * argv [])
{
	if (argc != 2){
		std::cout << "Usage: " << argv[0] << " <image_path>" << std::endl;
		exit(1);
	}

	char * image_path = argv[1];
	char * kernel = argv[2];

	CImg<pix_t> image(image_path);
	CImgDisplay display(image, image_path);
	Kernel::print(image);

	CImg< pix_t > grayscale = Kernel::grayscale(image);	
	CImgDisplay gray_display(grayscale, "Grayscale");
	
	CImg< pix_t > blured = Kernel::gaussian_blur(grayscale);
	CImgDisplay blured_display(blured, "Gaussian blur");
	Kernel::print(blured);

	CImg< pix_t > sobel_x = Kernel::sobel_x(grayscale);
	CImgDisplay sobel_x_display(sobel_x, "Sobel X");
	Kernel::print(sobel_x);

	CImg< pix_t > sobel_y = Kernel::sobel_y(grayscale);
	CImgDisplay sobel_y_display(sobel_y, "Sobel Y");
	Kernel::print(sobel_y);

	CImg< pix_t > sobel_gradient = Kernel::sobel_gradient(sobel_x, sobel_y);
	CImgDisplay sobel_gradient_display(sobel_gradient, "Sobel gradient");
	Kernel::print(sobel_gradient);


	while (!display.is_closed())
	{
		display.wait();
	}
}

