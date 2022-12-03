package app;

import java.awt.Color;
import java.awt.image.BufferedImage;

public class ImageProcessing
{
    private void loop(int height,int width,ImageRunnable runnable)
    {
        for(int y=0;y<height;y++)
        {
            for(int x=0;x<width;x++)
                runnable.run(x,y);
        }
    }
    public BufferedImage grayscale(BufferedImage image)
    {
        ImageRunnable imageRunnable=(x,y) ->
        {
            Color pixel=new Color(image.getRGB(x,y),true);
            int average=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
            Color newColor=new Color(average,average,average);
            image.setRGB(x,y,newColor.getRGB());
        };
        loop(image.getHeight(),image.getWidth(),imageRunnable);
        return image;
    }
    public BufferedImage bitmap(BufferedImage image,int threshold)
    {
        ImageRunnable runnable=(x,y) ->
        {
            Color pixel=new Color(image.getRGB(x,y),true);
            int average=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
            if(average>=threshold)
                image.setRGB(x,y,Color.WHITE.getRGB());
            else
                image.setRGB(x,y,Color.BLACK.getRGB());
        };
        loop(image.getHeight(),image.getWidth(),runnable);
        return image;
    }
    public BufferedImage increaseEachPixel(BufferedImage image,int value)
    {
        ImageRunnable runnable=(x,y) ->
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
                else
                    colors[i]=color;
            }
            Color newColor=new Color(colors[0],colors[1],colors[2]);
            image.setRGB(x,y,newColor.getRGB());
        };
        loop(image.getHeight(),image.getWidth(),runnable);
        return image;
    }
    public BufferedImage mirrorVertically(BufferedImage image)
    {
        ImageRunnable runnable=(x,y) ->
        {
            int pixel=image.getRGB(x,y);
            int otherSide=image.getRGB(image.getWidth()-1-x,y);
            image.setRGB(image.getWidth()-1-x,y,pixel);
            image.setRGB(x,y,otherSide);
        };
        loop(image.getHeight(),image.getWidth()/2,runnable);
        return image;
    }
    public BufferedImage mirrorHorizontally(BufferedImage image)
    {
        ImageRunnable runnable=(x,y) ->
        {
            int pixel=image.getRGB(x,y);
            int otherSide=image.getRGB(x,image.getHeight()-1-y);
            image.setRGB(x,image.getHeight()-1-y,pixel);
            image.setRGB(x,y,otherSide);
        };
        loop(image.getHeight()/2,image.getWidth(),runnable);
        return image;
    }
}