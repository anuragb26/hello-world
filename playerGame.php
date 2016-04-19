<?php
   function passCount($input1,$input2,$input3)
	{
		if(($input1 < 3 || $input1 > 1000) || ($input2 < 3 || $input2 > 1000) || !is_numeric($input3))
		return -1;
		$frequencyCount=array();
		for($i=0;$i<$input1;$i++)
		{
		    $frequencyCount[$i]=0;
		}
		$frequencyCount[0]=1;
		$currentPlayer=0;
		$noOfPasses=1;
		$gameOn=true;
		while($gameOn)
		{
		    if($frequencyCount[$currentPlayer]%2==0)
		    {
		        $diff=($input1-1)-$currentPlayer;
		        if($diff >= $input3)
		        {
		            $currentPlayer=$currentPlayer + $input3;
		            $frequencyCount[$currentPlayer]++;
		            if($frequencyCount[$currentPlayer]==$input2)
		            {
		                $gameOn=false;
		                break;
		            }
		            else
		            {
		                $noOfPasses++;
		            }
		        }
		        else
		        {
		            $remainingDiff=$input3-$diff;
		            $currentPlayer=$remainingDiff-1;
		            $frequencyCount[$currentPlayer]++;
		            if($frequencyCount[$currentPlayer]==$input2)
		            {
		                $gameOn=false;
		                break;
		            }
		            else
		            {
		                $noOfPasses++;
		            }
		            
		        }
		    }
		    else
		    {
		        $diff=$currentPlayer-$input3;
		        if($diff < 0)
		        {
		            $currentPlayer=$input1 - abs($diff);
		            $frequencyCount[$currentPlayer]++;
		            if($frequencyCount[$currentPlayer]==$input2)
		            {
		                $gameOn=false;
		                break;
		            }
		            else
		            {
		                $noOfPasses++;
		            } 
		        }
		        else
		        {
		            $currentPlayer=$currentPlayer - $input3;
		            $frequencyCount[$currentPlayer]++;
		            if($frequencyCount[$currentPlayer]==$input2)
		            {
		                $gameOn=false;
		                break;
		            }
		            else
		            {
		                $noOfPasses++;
		            }
		        }
		        
		    }
		}
		
		return $noOfPasses;
		
	}
?>
