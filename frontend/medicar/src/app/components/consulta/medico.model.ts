import {Especialidade} from './especialidade.model'

export interface Medico{
    id:string
    crm:number
    nome:string
    email:string
    telefone:string
    especialidade: Especialidade
}