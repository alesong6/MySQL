FROM php:8.2-fpm

RUN docker-php-ext-install pdo

RUN docker-php-ext-enable pdo

EXPOSE 8000

CMD ["php-fpm"]