package nogroup.passwordmaneger.repository;

import nogroup.passwordmaneger.model.User;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UserRepository extends MongoRepository<User, String> {
    User findByUsername(String username);
}
