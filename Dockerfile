FROM openjdk:19-jdk-alpine

LABEL authors="aviv"

RUN addgroup -S password-manager-group && adduser -S password-manager-user -G password-manager-group

USER password-manager-user

WORKDIR /password-manager

COPY ./target/PasswordManager-0.0.1-SNAPSHOT.jar .
EXPOSE 8080

ENTRYPOINT ["java", "-jar", "PasswordManager-0.0.1-SNAPSHOT.jar"]