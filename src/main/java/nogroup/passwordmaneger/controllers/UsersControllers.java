package nogroup.passwordmaneger.controllers;

import nogroup.passwordmaneger.model.User;
import nogroup.passwordmaneger.security.Sha;
import nogroup.passwordmaneger.service.UserService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UsersControllers {
    public UserService userService;

    public UsersControllers(UserService userService) {
        this.userService = userService;
    }
    @GetMapping("/signup")
    public String hello() {
        return "Hello";
    }

    @PostMapping("/signup")
    public String hello(@RequestParam String username, @RequestParam String password) {
        if(username==null || password==null){
            return "{\"success\": false, \"data\": \"\"}";
        }
        if(!userService.isUnique(username)){
            return "{\"success\": false, \"data\": \"\"}";
        }
        userService.save(new User(username, Sha.hash(password)));
        return "{\"success\": true, \"data\": \"\"}";
    }

    @GetMapping("/login")
    public String login(@RequestParam String username, @RequestParam String password) {
        if(username==null || password==null){
            return "{\"success\": false, \"data\": \"\"}";
        }
        User user = userService.findByUsername(username);
        if(user==null){
            return "{\"success\": false, \"data\": \"\"}";
        }
        if(!user.getPassword().equals(Sha.hash(password))){
            return "{\"success\": false, \"data\": \"\"}";
        }
        String response = "{\"success\": true, \"data\": \"" + user.getUserData() + "\"}";
        return response;
    }

}
