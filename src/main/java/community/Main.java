package community;

import java.io.File;
import java.io.IOException;

import org.apache.catalina.startup.Tomcat;

public class Main {
	private static final int PORT = 8080;
	private static final String BASE = ".";
	
	public static void main(String[] args) throws Exception {
        Tomcat tomcat = new Tomcat();
        tomcat.setBaseDir(createTempDir());
        tomcat.setPort(PORT);
        tomcat.getHost().setAppBase(BASE);
        tomcat.addWebapp("", BASE);
        tomcat.start();
        tomcat.getServer().await();
    }
	
	private static String createTempDir() {
        try {
            File tempDir = File.createTempFile("tomcat.", "." + PORT);
            tempDir.delete();
            tempDir.mkdir();
            tempDir.deleteOnExit();
            return tempDir.getAbsolutePath();
        } catch (IOException ex) {
            throw new RuntimeException(
                    "Unable to create tempDir. java.io.tmpdir is set to " + System.getProperty("java.io.tmpdir"),
                    ex
            );
        }
    }
}
