package app;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.lang.reflect.Method;
import java.util.List;
import java.lang.reflect.Parameter;
import java.lang.reflect.InvocationTargetException;

public class Main
{
    public static void main(String[] args)
    {
        try
	{
            if(args.length>2)
	    {
                String filePath=args[0];
                String outputFilePath=args[1];
                String methodName=args[2];
                ImageProcessing imageProcessing=new ImageProcessing();
		Method method=getMethod(methodName,ImageProcessing.class);
		Parameter[] methodParameters=method.getParameters();
		if(methodParameters.length-1==args.length-3)
		{
		    Object[] parameters=new Object[methodParameters.length];
		    parameters[0]=ImageIO.read(new File(filePath));
		    for(int i=1;i<parameters.length;i++)
			parameters[i]=Integer.valueOf(args[i+2]);
		    BufferedImage processedImage=(BufferedImage)method.invoke(imageProcessing,parameters);
		    ImageIO.write(processedImage, "png", new File(outputFilePath));
                    System.out.println("Done");
		}
		else
                    System.err.println("Wrong amount of arguments");
            }
	    else
                System.err.println("Missing arguments");
	    
	}
	catch(NoSuchMethodException e)
	{
	    System.err.println("Unknown operation");
	}
	catch(InvocationTargetException e)
	{
	    Throwable rootException=e.getTargetException();
	    System.err.println(rootException.getMessage());
	}
	catch(Exception e)
	{
	    System.err.println(e.getMessage());
	}
    }
    private static Method getMethod(String methodName,Class klass) throws NoSuchMethodException
    {
	for(Method method: klass.getMethods())
        {
            if(method.getName().equals(methodName))
            	return method;
	}
	throw new NoSuchMethodException();
    }
}