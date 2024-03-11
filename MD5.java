import java.io.FileInputStream;
import java.io.IOException;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {

    public static String md5File(String fileName) {
        try {
            MessageDigest md5Digest = MessageDigest.getInstance("MD5");
            try (DigestInputStream dis = new DigestInputStream(new FileInputStream(fileName), md5Digest)) {
                while (dis.read() != -1) {
                    // Read the file, the digest is updated automatically
                }
            }

            byte[] digestBytes = md5Digest.digest();

            StringBuilder hexDigest = new StringBuilder();
            for (byte b : digestBytes) {
                hexDigest.append(String.format("%02x", b));
            }

            return hexDigest.toString();
        } catch (NoSuchAlgorithmException | IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String md5String(String input) {
        try {
            MessageDigest md5Digest = MessageDigest.getInstance("MD5");
            byte[] inputBytes = input.getBytes();
            byte[] digestBytes = md5Digest.digest(inputBytes);

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
        String fileName = "example.txt";
        String fileHash = md5File(fileName);
        System.out.printf("MD5 hash of '%s' is: %s%n", fileName, fileHash);

        String strToHash = "I am Genius";
        String strHash = md5String(strToHash);
        System.out.printf("MD5 hash of '%s' is: %s%n", strToHash, strHash);
    }
}
