package nogroup.passwordmaneger.model;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;

@Getter
@Setter
public class User {
    @Id
    private String username;
    private String password;
    private String UserData;

    public User(String username, String password) {
        this.username = username;
        this.password = password;
        this.UserData= "";
    }
}
