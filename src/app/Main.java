package app;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.List;

public class Main
{
    public static void main(String[] args) throws IOException, InvocationTargetException, IllegalAccessException
    {
        List<String> methodsThatRequireInt=List.of("increaseEachPixel","bitmap");
        if(args.length<3)
            throw new IllegalArgumentException("Missing Arguments!");
        String filePath=args[0];
        String outputFilePath=args[1];
        String methodName=args[2];
        boolean requiresAdditionalParameter=methodsThatRequireInt.contains(methodName);
        if(requiresAdditionalParameter&&args.length<4)
            throw new IllegalArgumentException("Missing Arguments!");
        BufferedImage image = ImageIO.read(new File(filePath));
        ImageProcessing imageProcessing=new ImageProcessing();
        for(Method method: ImageProcessing.class.getDeclaredMethods())
        {
            if(method.getName().equals(methodName))
            {
                BufferedImage processedImage;
                if(requiresAdditionalParameter)
                {
                    int parameter=Integer.parseInt(args[3]);
                    processedImage=(BufferedImage)method.invoke(imageProcessing,image,parameter);
                }
                else
                    processedImage=(BufferedImage)method.invoke(imageProcessing,image);
                ImageIO.write(processedImage, "png", new File(outputFilePath));
                System.out.println("Done");
            }
        }
    }
}