class Address{
    constructor(street, city, zipCode){
        this.street=street;
        this.city=city;
        this.zipCode=zipCode;
        Object.freeze(this);
    }
}
class ImmutableExample{
    constructor(name, id, dateOfJoining, addresses){
        this.name=name;
        this.id=id;
        this.dateOfJoining=new Date(dateOfJoining.getTime());
        this.addresses=addresses.map(
            address=>new Address(address.street, address.city, address.zipCode)
        );
        Object.freeze(this);
        Object.freeze(this.addresses);
    }
    getName(){
        return this.name;
    }
    getId(){
        return this.id;
    }
    getDateOfJoining(){
        return new Date(this.dateOfJoining.getTime());
    }
    getAddresses(){
        return this.addresses.map(
            address=>new Address(address.street, address.city, address.zipCode)
        );
    }
}