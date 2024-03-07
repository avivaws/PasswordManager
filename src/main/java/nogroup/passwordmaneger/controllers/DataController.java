package nogroup.passwordmaneger.controllers;


import nogroup.passwordmaneger.model.User;
import nogroup.passwordmaneger.security.Sha;
import nogroup.passwordmaneger.service.UserService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataController {
    public UserService userService;

    public DataController(UserService userService) {
        this.userService = userService;
    }
    @PutMapping("/updatedata")
    public String updateData(@RequestParam String username, @RequestParam String password, @RequestParam String data) {
        if(username==null || password==null){
            return "Username or password is empty";
        }
        User user = userService.findByUsername(username);
        if(user==null){
            return "User with this username does not exist";
        }
        if(!user.getPassword().equals(Sha.hash(password))){
            return "Wrong password";
        }
        user.setUserData(data);
        userService.save(user);
        String response = "{\"success\": true, \"data\": \"" + user.getUserData() + "\"}";
        return response;
    }
}
