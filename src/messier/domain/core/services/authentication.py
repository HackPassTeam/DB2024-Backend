from messier.domain.core.adapters import AllAccounts, AllPersons
from messier.domain.core.services import IdentificationService
from messier.domain.core.services.notification import NotificationService
from messier.infrastructure.notifier import NotifierBackendEnum
from messier.infrastructure.notifier.backends.email.tasks import \
    EmailNotificationContentDTO
from messier.infrastructure.security.confirmation_code import \
    generate_confirmation_code
from messier.infrastructure.security.password import verify_password, get_password_hash

from messier.domain.core.models.person.account import Account
from messier.domain.core.models.person.person import Person
from messier.domain.core.exceptions.authentication import (
    AuthenticationError,
    LoginAlreadyOccupiedError,
)

from messier.infrastructure.bases.service import BaseService


class AuthenticationService(BaseService):
    def __init__(
            self,
            all_accounts: AllAccounts,
            notification_service: NotificationService,
            identification_service: IdentificationService,
            all_persons: AllPersons,
    ):
        self.notification_service = notification_service
        self.identification_service = identification_service
        self.all_accounts = all_accounts
        self.all_persons = all_persons

    async def register_account(
            self,
            email: str,
            password: str,
            person: Person,
    ) -> Account:
        """

        :param email:
        :param password:
        :param person:
        :raise LoginAlreadyOccupiedError
        :return:
        """
        is_login_occupied = await self.all_accounts.is_email_occupied(email)

        if is_login_occupied:
            raise LoginAlreadyOccupiedError()

        password_hash = get_password_hash(password)

        account = await self.all_accounts.create(
            email=email,
            password_hash=password_hash,
            person=None,
        )
        person.account = account
        await self.all_persons.save(person)

        return account

    async def authenticate(
            self,
            login: str,
            password: str,
    ) -> Account:
        """

        :param login:
        :param password:
        :raise AuthenticationError:
        :return:
        """
        account = await self.all_accounts.with_login(login)

        if account is None:
            raise AuthenticationError()

        is_verified = verify_password(password, account.password_hash)

        if not is_verified:
            raise AuthenticationError()

        return account
