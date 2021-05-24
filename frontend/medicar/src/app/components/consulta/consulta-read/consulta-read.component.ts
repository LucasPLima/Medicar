import { Component, OnInit, } from '@angular/core';

import { AuthService } from 'src/app/auth/auth.service';
import { ConsultaItem } from '../consulta-item.model';
import { Consulta } from '../consulta.model';

import { ConsultaService } from '../consulta.service';


@Component({
  selector: 'app-consulta-read',
  templateUrl: './consulta-read.component.html',
  styleUrls: ['./consulta-read.component.css']
})
export class ConsultaReadComponent implements OnInit {
  consultas: ConsultaItem[] = []
  userFullname:string=""

  displayedColumns = ['especialidade', 'profissional','data','hora','action'];

  constructor(private authService: AuthService,
              private consultaService: ConsultaService) {}

  ngOnInit(){
    this.userFullname = this.authService.getUserName()
    this.consultaService.list().subscribe(
      (consultas)=>{
        console.log(consultas)
        this.consultas = consultas.map((consulta)=>this.consultaToItem(consulta)) 
      }
    )
  }

  private consultaToItem(consulta:Consulta):ConsultaItem{
    return {
              id: consulta.id.toString(),
              data: consulta.dia,
              especialidade: consulta.medico.especialidade.nome,
              hora: consulta.horario,
              profissional: consulta.medico.nome
           }
  }
  
  deletarConsulta(id:string){
    console.log(id)
  }

  openConsultaCreateDialog():void{

  }
  
}
