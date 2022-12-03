package app;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Main
{
    public static void main(String[] args) throws IOException
    {
        String filePath="c:\\example.png";
        String outputFilePath="c:\\output.png";
        BufferedImage image = ImageIO.read(new File(filePath));
        ImageProcessing imageProcessing=new ImageProcessing();
        BufferedImage processedImage=imageProcessing.grayscale(image);
        ImageIO.write(processedImage, "png", new File(outputFilePath));
    }
}