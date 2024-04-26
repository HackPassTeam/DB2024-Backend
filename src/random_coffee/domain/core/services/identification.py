from random_coffee.domain.core.adapters.identification_session import (
    AllIdentificationSessions,
)
from random_coffee.domain.core.adapters.person import AllPersons
from random_coffee.domain.core.models.person.person import Person
from random_coffee.domain.core.models.person.account import Account
from random_coffee.infrastructure.security.confirmation_code import (
    generate_confirmation_code,
    get_confirmation_code_hash,
    verify_confirmation_code,
)
from random_coffee.domain.core.exceptions.identification import (
    UnknownEmailDomainError,
    IdentificationConfirmationNotVerified,
)
from random_coffee.domain.core.services.access import AccessService
from random_coffee.domain.core.models.identification_session import (
    IdentificationSession,
    IdentificationSessionStatusEnum,
)
from random_coffee.domain.core import models

from random_coffee.infrastructure.bases.service import BaseService


class IdentificationService(BaseService):
    def __init__(
            self,
            all_persons: AllPersons,
            access_service: AccessService,
            all_identification_sessions: AllIdentificationSessions,
    ):
        self.all_persons = all_persons
        self.all_identification_sessions = all_identification_sessions
        self.access_service = access_service

    async def create_person(
            self,
            full_name: str,
    ) -> Person:
        person = await self.all_persons.create(
            full_name=full_name,
        )
        return person

    async def create_identification_session(
            self,
            account: Account,
            person: Person,
            confirmation_code: int,
    ) -> IdentificationSession:
        email_domain = account.email.split("@")[1]
        confirmation_code_hash = get_confirmation_code_hash(confirmation_code)
        identification_session = await self.all_identification_sessions.create(
            account_id=account.id,
            person_id=person.id,
            confirmation_code_hash=confirmation_code_hash,
        )
        return identification_session

    async def confirm_identification(
            self,
            account: Account,
            confirmation_code: str,
    ) -> Person:
        sessions = await self.all_identification_sessions.by_account(
            account_id=account.id,
        )
        for i in sessions:
            if verify_confirmation_code(confirmation_code, i.confirmation_code_hash):
                i.status = IdentificationSessionStatusEnum.APPROVED
                await self.all_identification_sessions.save(i)
                person = await self.all_persons.with_id(i.person_id)
                person.account_id = account.id
                await self.all_persons.save(person)
                await self.organisation_service.create_employee(
                    person=person,
                    organisation_id=i.organisation_id,
                )
                return person
        else:
            raise IdentificationConfirmationNotVerified()
