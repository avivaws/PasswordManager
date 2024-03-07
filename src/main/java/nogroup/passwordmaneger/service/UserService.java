package nogroup.passwordmaneger.service;

import nogroup.passwordmaneger.model.User;

public interface UserService {
    boolean isUnique(String username);

    User findByUsername(String username);

    void save(User user);

}
