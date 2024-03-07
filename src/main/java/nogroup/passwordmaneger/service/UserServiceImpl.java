package nogroup.passwordmaneger.service;

import nogroup.passwordmaneger.model.User;
import nogroup.passwordmaneger.repository.UserRepository;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService{

    private final UserRepository userRepository;

    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    @Override
    public boolean isUnique(String username) {
        return userRepository.findByUsername(username) == null;
    }

    @Override
    public void save(User user) {
        userRepository.save(user);
    }

    public User findByUsername(String username){
        return userRepository.findByUsername(username);
    }
}
