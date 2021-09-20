package app;

import java.awt.*;
import java.awt.image.BufferedImage;

public class ImageProcessing
{
    public BufferedImage grayscale(BufferedImage image)
    {
        for(int y=0;y<image.getHeight();y++)
        {
            for(int x=0;x<image.getWidth();x++)
            {
                Color pixel=new Color(image.getRGB(x,y),true);
                int average=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
                Color newColor=new Color(average,average,average);
                image.setRGB(x,y,newColor.getRGB());
            }
        }
        return image;
    }
    public BufferedImage increaseEachPixel(BufferedImage image,int value)
    {
        for(int y=0;y<image.getHeight();y++)
        {
            for(int x=0;x<image.getWidth();x++)
            {
                Color pixel=new Color(image.getRGB(x,y),true);
                int[] colors={pixel.getRed(),pixel.getGreen(),pixel.getBlue()};
                for(int i=0;i<colors.length;i++)
                {
                    int color=colors[i]+value;
                    if(color>255)
                        colors[i]=255;
                    else if(color<0)
                        colors[i]=0;
                }
                Color newColor=new Color(colors[0],colors[1],colors[2]);
                image.setRGB(x,y,newColor.getRGB());
            }
        }
        return image;
    }
    public BufferedImage bitmap(BufferedImage image,int threshold)
    {
        for(int y=0;y<image.getHeight();y++)
        {
            for(int x=0;x<image.getWidth();x++)
            {
                Color pixel=new Color(image.getRGB(x,y),true);
                int average=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
                if(average>=threshold)
                    image.setRGB(x,y,Color.WHITE.getRGB());
                else
                    image.setRGB(x,y,Color.BLACK.getRGB());
            }
        }
        return image;
    }
}