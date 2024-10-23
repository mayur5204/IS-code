import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Hash {

    public static String calculateMD5(String input) {
        try {
            // Get an instance of the MD5 MessageDigest
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Update the digest with the byte array of the input string
            md.update(input.getBytes());

            // Compute the hash
            byte[] digest = md.digest();

            // Convert the byte array to a hexadecimal string
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }

            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        String text = "Hello, World!";
        String md5Hash = calculateMD5(text);
        System.out.println("MD5 Hash: " + md5Hash);
    }
}