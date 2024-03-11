import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SHA1 {

    public static String sha1(String message) {
        try {
            MessageDigest sha1Digest = MessageDigest.getInstance("SHA-1");
            byte[] messageBytes = message.getBytes(StandardCharsets.UTF_8);
            sha1Digest.update(messageBytes);
            byte[] digestBytes = sha1Digest.digest();
            
            StringBuilder hexDigest = new StringBuilder();
            for (byte b : digestBytes) {
                hexDigest.append(String.format("%02x", b));
            }
            
            return hexDigest.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        String message = "Hello, World!";
        String hashedMessage = sha1(message);
        System.out.printf("SHA-1 hash of '%s' is: %s%n", message, hashedMessage);
    }
}